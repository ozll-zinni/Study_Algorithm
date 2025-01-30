function solution(h1, m1, s1, h2, m2, s2) {
  const SECONDS_ANGLE = 360 / 60;
  const MINUTES_ANGLE = 360 / 60 / 60;
  const HOURS_ANGLE = 360 / 12 / 60 / 60;

  let cnt = 0;

  let start_time = h1 * 60 * 60 + m1 * 60 + s1;

  let end_time = h2 * 60 * 60 + m2 * 60 + s2;

  const start_hour_angle = (start_time * HOURS_ANGLE) % 360;
  const start_minute_angle = (start_time * MINUTES_ANGLE) % 360;
  const start_seconds_angle = (start_time * SECONDS_ANGLE) % 360;

  if (start_seconds_angle === start_hour_angle) cnt++;
  if (start_seconds_angle === start_minute_angle) cnt++;
  if (
    start_seconds_angle === start_hour_angle &&
    start_seconds_angle === start_minute_angle
  )
    cnt--;

  while (start_time < end_time) {
    const current_hours_angle = (start_time * HOURS_ANGLE) % 360;
    const current_minutes_angle = (start_time * MINUTES_ANGLE) % 360;
    const current_seconds_angle = (start_time * SECONDS_ANGLE) % 360;

    const next_time = start_time + 1;

    const next_hours_angle = (next_time * HOURS_ANGLE) % 360 || 360;
    const next_minutes_angle = (next_time * MINUTES_ANGLE) % 360 || 360;
    const next_seconds_angle = (next_time * SECONDS_ANGLE) % 360 || 360;

    if (
      current_seconds_angle < current_hours_angle &&
      next_seconds_angle >= next_hours_angle
    )
      cnt++;
    if (
      current_seconds_angle < current_minutes_angle &&
      next_seconds_angle >= next_minutes_angle
    )
      cnt++;
    if (
      next_seconds_angle === next_hours_angle &&
      next_seconds_angle === next_minutes_angle
    )
      cnt--;

    start_time = next_time;
  }

  return cnt;
}