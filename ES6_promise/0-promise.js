function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = Math.random() > 0.5;

      if (success) {
        resolve(true);
      }
    }, 300);
  });
}

export default getResponseFromAPI;
