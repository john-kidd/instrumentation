import createUUID from './uuid';

export function timer(logInfo) {
    return (action, getDescription) => {
        const start = new Date();
        action();
        const end = new Date();        
        const duration = Math.floor(end - start) / (1000);
        logInfo(`DURATION: ${getDescription()} took ${duration}`); 
    }
}

export function wrap(logInfo) {
    return (action, getDescription) => {
        const action_timer = timer(logInfo);
        logInfo(`BEGIN: ${getDescription()}`);
        action_timer(action, getDescription);
        logInfo(`END: ${getDescription()}`);
        logInfo('\n');
    }
}

export function handleError(logInfo) {
    return (action, getDescription) => {
        const action_wrap = wrap(logInfo);
        try {
            action_wrap(action, getDescription);
        } catch(ex) {
            const correlationId = createUUID();
            logInfo(ex);
            logInfo(`Correlation Id ${correlationId}`);
            logInfo(`FAILED: ${getDescription()}`);
            logInfo('\n');
            throw new Error(`An error has occurred. Please contact support with correlation Id ${correlationId}`);
        }
    }
}