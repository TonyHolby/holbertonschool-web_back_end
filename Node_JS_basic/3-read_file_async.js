const file_system = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        file_system.readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.split('\n').filter(line => line.trim() !== '');

            if (lines.length <= 1) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const fields = {};

            for (let i = 1; i < lines.length; i++) {
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

            const number_of_students = Object.values(fields).reduce((acc, curr) => acc + curr.length, 0);
            console.log(`Number of students: ${number_of_students}`);

            for (const [field, students] of Object.entries(fields)) {
                console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
            }

            resolve();
        });
    });
}

module.exports = countStudents;
