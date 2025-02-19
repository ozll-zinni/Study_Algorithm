function solution(schedules, timelogs, startday) {
    var winner = 0;

    for (let i = 0; i < schedules.length; i++) {
        let scheduleTime = schedules[i];
        let baseHour = Math.floor(scheduleTime / 100);
        let baseMinute = scheduleTime % 100;

        let latestHour = baseHour;
        let latestMinute = baseMinute + 10;
        if (latestMinute >= 60) {
            latestHour += 1;
            latestMinute -= 60;
        }
        let latestTime = latestHour * 100 + latestMinute;

        let isLate = false;
        for (let j = 0; j < 7; j++) {
            let currentDay = (j + startday - 1) % 7 + 1;
            if (currentDay === 6 || currentDay === 7) continue;

            if (timelogs[i][j] > latestTime) {
                isLate = true;
                break;
            }
        }

        if (!isLate) winner++;
    }

    return winner;
}
