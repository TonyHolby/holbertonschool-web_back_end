/**
 * A function to return the number of arguments passed to it
 * using the rest parameter syntax.
 * @param  {...any} args
 * @returns
 */
export default function returnHowManyArguments(...args) {
  return args.length;
}
