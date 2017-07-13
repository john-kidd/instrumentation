import createUUID from './uuid';

export function logTime(logInfo) {
    return (query, getDescription) => {
        const start = new Date();
        const result = query();
        const end = new Date();        
        const duration = Math.floor(end - start) / (1000);
        logInfo(`DURATION: ${getDescription()} took ${duration}`); 
        return result;
    }
}

export function logWrap(logInfo) {
    return (query, getDescription) => {
        const query_timer = logTime(logInfo);
        logInfo(`BEGIN: ${getDescription()}`);
        const result = query_timer(query, getDescription);
        logInfo(`END: ${getDescription()}`);
        logInfo('\n');
        return result;
    }
}

export function handleError(logError, logInfo) {
    return (action, getDescription) => {
        const action_wrap = logWrap(logInfo);
        try {
            action_wrap(action, getDescription);
        } catch(ex) {
            logError(ex);
            const correlationId = createUUID();
            logInfo(`Correlation Id: ${correlationId}`);
            logInfo(`FAILED: ${getDescription()}`);
            logInfo('\n');
            throw new Error(`An error has occurred. Please contact support with correlation Id ${correlationId}`);
        }
    }
}