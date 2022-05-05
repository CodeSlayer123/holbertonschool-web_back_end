export default function handleResponseFromAPI(promise){
    let resolved = {
        'status': 200,
        'body': 'success',
      };
    return promise.then(() => (resolved))
    .catch(() => Error())
    .finally(() => console.log("Got a response from the API"))


}