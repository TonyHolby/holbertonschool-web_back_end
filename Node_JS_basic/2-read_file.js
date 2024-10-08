const fs = require('fs');

function countStudents(path) {
  try {
    const file = fs.readFileSync(path, 'utf8');

    const lines = file.trim().split('\n');

    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    const fields = {};

    for (let i = 1; i < lines.length; i += 1) {
      const line = lines[i].trim();

      if (line) {
        const student = line.split(',');
        const firstName = student[0];
        const field = student[3];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    }

    const numberOfStudents = Object.values(fields).reduce((acc, curr) => acc + curr.length, 0);
    console.log(`Number of students: ${numberOfStudents}`);

    for (const [field, students] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
