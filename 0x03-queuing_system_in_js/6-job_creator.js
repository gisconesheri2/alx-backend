import kue from 'kue';

const jobData = {
  phoneNumber: '1234567',
  message: 'true dat'
};

const queue = kue.createQueue({ name: 'push_notification_code' });

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) console.log('Notification job created:', job.id);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
