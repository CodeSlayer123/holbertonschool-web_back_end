function createPushNotificationsJobs(jobs, queue){
    if (!Array.isArray(jobs)){
        throw new Error('Jobs is not an array')
    }

    for (const i of jobs){
        try{
            const job = queue.create('push_notification_code_3', i).save((error) => {
                if (!error){
                    console.log(`Notification job created: ${job.id}`)
                }
            })
            .on('complete', () => {
                console.log(`Notification job ${job.id} completed`)
            })
            .on('failed', (error) => {
                console.log(`Notification job ${job.id} failed: ${error}`)
            })
            .on('progress', (progress) => {
                console.log(`Notification job ${job.id} ${progress}% complete`)
            })
        } catch (error) {

        }

    }
}

module.exports = createPushNotificationsJobs