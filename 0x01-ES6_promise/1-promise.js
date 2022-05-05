export default function getFullResponseFromAPI(success){
    return new Promise((resolve, reject) => {
        if (success === true){
            let object = {
                status: 200,
                body: 'Success',
              };
            resolve(object);
        }
        else{
            reject(new Error("The fake API is not working currently"))
        }
    })
}