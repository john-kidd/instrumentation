import {expect} from 'chai';
import {logTime, logWrap, handleError} from './execute_around_command'

describe('logTime', () => {
    it('DURATION of action is added to log', () => {
        const EXPECTED = 'DURATION';
        let actual = null;
        const target = logTime(message => actual += message);
        target(() => console.log('executed'), () => 'an action');
        expect(actual).to.contain(EXPECTED);
    });
});

describe('logWrap', () => {
    let actual = null;
    const target = logWrap(message => actual += message);
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
        try {
            target(() => { throw new Error('an error has occurred'); }, () => 'an action');
        } catch(ex){
            // TODO: what is a more elegant way to handle this???
        }
    });
    it('FAILED is added to log when an error is caught', () => {
        const EXPECTED = 'FAILED';
        expect(actual).to.contain(EXPECTED);
    })
    it('Correlation Id is part of log', () => {
        const EXPECTED = 'Correlation Id';
        expect(actual).to.contain(EXPECTED);
    })
});