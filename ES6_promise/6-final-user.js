import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  if (typeof firstName !== 'string' || typeof lastName !== 'string' || typeof fileName !== 'string') {
    return '';
  }
  
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPhotoPromise = uploadPhoto(fileName);

  const promisesSettled = await Promise.allSettled([signUpPromise, uploadPhotoPromise]);

  return promisesSettled.map((promiseResult) => {
    if (promiseResult.status === 'fulfilled') {
      return {
        status: promiseResult.status,
        value: promiseResult.value,
      };
    }

    return {
      status: promiseResult.status,
      value: promiseResult.reason,
    };
  });
}
