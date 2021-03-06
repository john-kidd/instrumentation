export function validateInput(logInfo, description, inputValue) {
    if (!inputValue)
        throw new Error('Invalid input');
    logInfo(`INPUT ${description}\n${inputValue.toString()}`);
}

export function validateOutput(logInfo, description, inputValue) {
    if (!inputValue)
        throw new Error('Invalid output');
    logInfo(`OUTPUT ${description}\n${inputValue.toString()}`);
}