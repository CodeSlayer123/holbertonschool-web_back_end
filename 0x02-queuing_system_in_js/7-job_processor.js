const kue = require('kue')
const que = kue.createQueue()


const blacklisted = ['4153518780', '4153518781']

function sendNotification(phoneNumber, message, job, done ){
    job.progress(0, 100);
    if (blacklisted.includes(phoneNumber)){
        var error = new Error(`Phone number ${phoneNumber} is blacklisted`)
        job.failed().error(error)
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`))
    }
    job.progress(50, 100)
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
    done()
}

que.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done)
});