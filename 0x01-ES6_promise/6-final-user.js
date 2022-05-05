import signUpUser from './4-user-promise'
import uploadPhoto from './5-photo-reject'

export default async function handleProfileSignup(firstName, lastName, fileName) {


    const prom1 = await signUpUser(firstName, lastName).then((prom) => (
        {'status': 'fulfilled',
        'vallue': prom,}
    ))

    const prom2 = await uploadPhoto(fileName).catch((prom) => (
        {'status': 'rejected',
        'value': prom.toString(),}

    ))
    return Promise.resolve([prom1, prom2])
}