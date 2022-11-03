const kue = require('kue')
const job_data =
{
    phoneNumber: "12345",
    message: "Hello there",
}
const que = kue.createQueue()
const job = que.create('push_notification_code', job_data).save((error) => {
    if (!error){
        console.log(`Notification job created: ${job.id}`)
    }
    else {
        console.log('Notification job failed')
    }
})
.on('complete', () => {
    console.log('Notification job completed')
})
