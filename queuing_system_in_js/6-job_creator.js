const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1234567890',
    message: 'This is a test notification',
};

const job = queue.create('push_notification_code', jobData);

job.save((err) => {
    if (err) {
        console.error('Error saving job:', err);
    } else {
        console.log(`Notification job created: ${job.id}`);
    }
});

job.on('complete', () => {
    console.log('Notification job completed');
}).on('failed', (err) => {
    console.log(`Notification job failed: ${err}`);
});

queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
});
