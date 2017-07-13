import createUUID from './uuid';

export function logTime(logInfo) {
    return (action, getDescription) => {
        const start = new Date();
        action();
        const end = new Date();        
        const duration = Math.floor(end - start) / (1000);
        logInfo(`DURATION: ${getDescription()} took ${duration}`); 
    }
}

export function logWrap(logInfo) {
    return (action, getDescription) => {
        const action_timer = logTime(logInfo);
        logInfo(`BEGIN: ${getDescription()}`);
        action_timer(action, getDescription);
        logInfo(`END: ${getDescription()}`);
        logInfo('\n');
    }
}

export function handleError(logError, logInfo) {
    return (action, getDescription) => {
        const action_wrap = logWrap(logInfo);
        try {
            action_wrap(action, getDescription);
        } catch(ex) {
            const correlationId = createUUID();
            logError(ex);
            logInfo(`Correlation Id: ${correlationId}`);
            logInfo(`FAILED: ${getDescription()}`);
            logInfo('\n');
            throw new Error(`An error has occurred. Please contact support with correlation Id ${correlationId}`);
        }
    }
}