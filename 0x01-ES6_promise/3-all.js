import {uploadPhoto, createUser} from './utils'


export default function handleProfileSignup(){
    const prom1 = uploadPhoto()
    const prom2 = createUser()

    Promise.all([prom1, prom2]).then((prom1) => {
        console.log(prom1[0].body, prom1[1].firstName, prom1[1].lastName);
    })
    .catch(() => {
        console.log("Signup system offline")
    })


}