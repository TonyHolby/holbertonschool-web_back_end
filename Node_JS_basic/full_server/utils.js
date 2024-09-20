import fs from 'fs';

export const readDatabase = async (databasePath) => {
    try {
        const data = await fs.readFile(databasePath, 'utf8');

        const lines = data.split('\n').filter((line) => line.trim() !== '');

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
        const result = {
            numberOfStudents,
            studentsByField: fields
        };

        return result;
    } catch (err) {
        throw new Error('Cannot load the database');
    }
};
