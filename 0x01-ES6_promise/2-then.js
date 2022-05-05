export default function handleResponseFromAPI(promise){
    let resolved = {
        'status': 200,
        'body': 'Success',
      };
    return promise.then(() => (resolved))
    .catch(() => new Error())
    .finally(() => console.log("Got a response from the API"))


}