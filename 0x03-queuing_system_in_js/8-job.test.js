import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job';
import { expect } from 'chai';
import { describe, it, before, afterEach, after } from 'mocha';

const queue = createQueue();
describe('createPushNotificationsJobs', () => {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('tests when jobs is not array', function () {
    expect(() => createPushNotificationsJobs('rest', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('creation of two jobs', function () {
    const jobs = [
      {
        phoneNumber: 2322332,
        message: 'reset'
      },
      {
        phoneNumber: 999999,
        message: 'all good'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    // console.log(queue.testMode.jobs)
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    queue.testMode.jobs.forEach(job => {
      expect(job.type).to.be.equal('push_notification_code_3');
      expect(job.data.phoneNumber).to.be.a('number');
      expect(job.data.message).to.be.a('string');
    });
  });
});
