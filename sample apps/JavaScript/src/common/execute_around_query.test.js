import {expect} from 'chai';
import {logTime, logWrap, handleError} from './execute_around_query'

describe('timer', () => {
    it('DURATION of query is added to log', () => {
        const EXPECTED = 'DURATION';
        let actual = null;
        const target = logTime(message => actual += message);
        target(() => 'a value', () => 'a query');
        expect(actual).to.contain(EXPECTED);
    });
    it('Query returns expected result', () => {
        const EXPECTED = 'a value';
        const target = logTime(console.log);
        const actual = target(() => EXPECTED, () => 'a query');
        expect(actual).to.contain(EXPECTED);
    });
});

describe('wrap', () => {
    let actual = null;
    const target = logWrap(message => actual += message);
    beforeEach(() => {
        target(() => console.log('executed'), () => 'an action');
    });
    it('BEGIN query is added to log', () => {
        const EXPECTED = 'BEGIN';
        expect(actual).to.contain(EXPECTED);
    });
    it('END query is added to log', () => {
        const EXPECTED = 'END';
        expect(actual).to.contain(EXPECTED);
    });
});

describe('handleError', () => {
    let actual = null;
    const target = handleError(message => actual += message);
    beforeEach(() => {
        try {
            target(() => { throw new Error('an error has occurred'); }, () => 'an query');
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