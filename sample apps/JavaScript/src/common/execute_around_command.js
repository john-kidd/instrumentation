export function time(logInfo) {
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
        const timer = time(logInfo);
        logInfo(`BEGIN: ${getDescription()}`);
        timer(action, getDescription);
        logInfo(`END: ${getDescription()}`);
    }
}

export function handleError(logInfo) {
    return (action, getDescription) => {
        const wrapper = wrap(logInfo);
        try {
            wrapper(action, getDescription);
        } catch(ex) {
            logInfo(`FAILED: ${getDescription()}`);
        }
    }
}