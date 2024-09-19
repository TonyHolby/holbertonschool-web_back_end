const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const fields = {};

      for (let i = 1; i < lines.length; i += 1) {
        const line = lines[i].trim();

        if (line) {
          const student = line.split(',');

          const firstName = student[0].trim();
          const field = student[3].trim();

          if (firstName && field) {
            if (!fields[field]) {
              fields[field] = [];
            }

            fields[field].push(firstName);
          }
        }
      }

      const numberOfStudents = Object.values(fields).reduce((acc, curr) => acc + curr.length, 0);
      
      let output = `Number of students: ${numberOfStudents}\n`;
      for (const [field, students] of Object.entries(fields)) {
        output += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      }

      resolve(output.trim());
    });
  });
}

module.exports = countStudents;
