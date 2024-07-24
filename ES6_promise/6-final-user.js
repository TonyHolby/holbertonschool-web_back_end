import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPhotoPromise = uploadPhoto(fileName);

  const promisesettled = await Promise.allSettled([signUpPromise, uploadPhotoPromise]);

  return promisesettled.map((promises) => {
    const result = { status: promises.status };
    if (promises.status === 'fulfilled') {
      result.value = promises.value;
    } else {
      result.value = promises.reason;
    }
    return result;
  });
}
