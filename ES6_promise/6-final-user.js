import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPhotoPromise = uploadPhoto(fileName);

  const promisesettled = await Promise.allSettled([signUpPromise, uploadPhotoPromise]);

  return promisesettled.map((promiseResult) => {
    if (promiseResult === 'fulfilled') {
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
