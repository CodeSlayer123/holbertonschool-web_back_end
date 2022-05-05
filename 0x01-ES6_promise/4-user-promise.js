export default function signUpUser(firstName, lastName) {
  return new Promise((resolve) => {
    const myDude = {
      firstName,
      lastName,
    };
    resolve(myDude);
  });
}
