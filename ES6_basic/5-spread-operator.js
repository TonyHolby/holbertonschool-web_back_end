/**
 * A function that concatenates 2 arrays and each character
 * of a string in using spread syntax.
 * @param {list} array1 
 * @param {list} array2 
 * @param {string} string 
 * @returns 
 */
export default function concatArrays(array1, array2, string) {
    return [...array1, ...array2, ...string];
}
