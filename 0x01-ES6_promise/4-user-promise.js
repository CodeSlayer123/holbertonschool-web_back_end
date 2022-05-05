import {uploadPhoto, createUser} from './utils'


export default function signUpUser(firstName, lastName){
    return new Promise((resolve, reject) => {
        let myDude = {
            firstName,
            lastName,
        }
        resolve(myDude);

    })


}