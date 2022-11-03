import createPushNotificationsJobs from './8-job.js';
const kue = require('kue')
const queue = kue.createQueue()

const expect = require('chai').expect;

describe('createPushNotificationsJobs', () => {
    before(() => {
        queue.testMode.enter()
    })
    afterEach(() => {
        queue.testMode.clear()
    })
    after(() => {
        queue.testMode.exit()
    })

    it('tests for errors', () => {
        expect(() => createPushNotificationsJobs('Cheeseburger', queue)).to.throw(Error, 'Jobs is not an array');
        expect(() => createPushNotificationsJobs(42, queue)).to.throw(Error, 'Jobs is not an array');
        expect(() => createPushNotificationsJobs(null, queue)).to.throw(Error, 'Jobs is not an array');

    });
    it('tests for creating jobs successfully', () => {
        const list = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4815162342',
                message: 'This is the code 4321 to verify your account'
            }
        ];
        createPushNotificationsJobs(list, queue)
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');

        expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('4153518780');
        expect(queue.testMode.jobs[0].data.message).to.equal('This is the code 1234 to verify your account');

        expect(queue.testMode.jobs[1].data.phoneNumber).to.equal('4815162342');
        expect(queue.testMode.jobs[1].data.message).to.equal('This is the code 4321 to verify your account');

    });

  });