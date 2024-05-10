export default function getFullResponseFromAPI(bool) {
  return new Promise((resolve, reject) => {
    if (bool) {
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
