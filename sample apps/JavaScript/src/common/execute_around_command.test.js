import {expect} from 'chai';
import {time, wrap, handleError} from './execute_around_command'

describe('time', () => {
    it('DURATION of action is added to log', () => {
        const EXPECTED = 'DURATION';
        let actual = null;
        const target = time(message => actual += message);
        target(() => console.log('executed'), () => 'an action');
        expect(actual).to.contain(EXPECTED);
    });
});

describe('wrap', () => {
    let actual = null;
    const target = wrap(message => actual += message);
    beforeEach(() => {
        target(() => console.log('executed'), () => 'an action');
    });
    it('BEGIN action is added to log', () => {
        const EXPECTED = 'BEGIN';
        expect(actual).to.contain(EXPECTED);
    });
    it('END action is added to log', () => {
        const EXPECTED = 'END';
        expect(actual).to.contain(EXPECTED);
    });
});

describe('handleError', () => {
    let actual = null;
    const target = handleError(message => actual += message);
    beforeEach(() => {
        target(() => { throw new Error('an error has occurred'); }, () => 'an action');
    });
    it('FAILED is added to log when an error is caught', () => {
        const EXPECTED = 'FAILED';
        expect(actual).to.contain(EXPECTED);
    })
});