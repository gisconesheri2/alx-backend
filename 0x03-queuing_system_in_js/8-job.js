
function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((jobData) => {
    const job = queue.createJob('push_notification_code_3', jobData);
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });
    job.on('failed', (err, _) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });
    job.on('progress', (progress, _) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
    job.save();
  });
}

export default createPushNotificationsJobs;
