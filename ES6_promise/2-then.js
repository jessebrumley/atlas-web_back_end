export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({
      body: 'success',
      status: 200,
    }))
    .catch((error) => {
      console.error('Error fetching data:', error);
      return { error: 'An error occurred while fetching data.' };
    })
    .finally(() => console.log('Got a response from the API'));
}
