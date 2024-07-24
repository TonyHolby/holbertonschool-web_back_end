import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);

  return Promise.allSettled([signUpPromise, uploadPromise])
    .then((results) => results.map((promisesettled) => {
      if (promisesettled.status === 'fulfilled') {
        return { status: promisesettled.status, value: promisesettled.value };
      }
      return { status: promisesettled.status, value: promisesettled.reason };
    }));
}

export default handleProfileSignup;
