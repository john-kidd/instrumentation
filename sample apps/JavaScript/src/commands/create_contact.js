import {validateInput} from '../common/guard';

export function createContact(logInfo, description) {
    return (contact) => {
        validateInput(logInfo, description, contact);
        // do stuff here...

    };
}