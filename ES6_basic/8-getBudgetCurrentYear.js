/**
 * A function that returns the current year.
 * @returns the current year.
 */
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

/**
 * A function that returns the object budget for the current year
 * with the given income, GDP, and capita.
 * @param {number} income - The income for the current year.
 * @param {number} gdp - The GDP for the current year.
 * @param {number} capita - The GDP per capita for the current year.
 * @returns {Object} the object budget.
 */
export default function getBudgetForCurrentYear(income, gdp, capita) {
  const currentYear = getCurrentYear();

  const budget = {
    [`income-${currentYear}`]: income,
    [`gdp-${currentYear}`]: gdp,
    [`capita-${currentYear}`]: capita,
  };

  return budget;
}
