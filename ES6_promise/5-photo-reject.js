export default function uploadPhoto(fileName) {
  const uploadProcess = new Promise((resolve, reject) => {
    reject(new Error(`${fileName} cannot be processed.`));
  });
  return uploadProcess;
}
