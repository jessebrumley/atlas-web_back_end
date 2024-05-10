import { uploadPhoto, createUser } from 'utils.js';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoResult, userResult]) => {
      console.log(`Photo uploaded successfully: ${photoResult.body}`);
      console.log(`User created successfully: ${userResult.firstName} ${userResult.lastName}`);
    })
    .catch((error) => {
      console.error('Signup system offline', error);
    });
}
