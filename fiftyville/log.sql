-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE year=2023 AND month='7' AND day=28 AND street='Humphrey Street' AND description LIKE '%duck%';
SELECT * FROM interviews WHERE year=2023 AND month=7 AND day=28 AND transcript LIKE '%bakery%';
SELECT * FROM atm_transactions WHERE year=2023 AND month=7 AND day=28;
SELECT * FROM bakery_security_logs WHERE year=2023 AND month=7 AND day=28 AND hour=10;
SELECT * FROM phone_calls WHERE year=2023 AND month=7 AND day=28 AND duration<60;
SELECT * FROM flights WHERE year=2023 AND month=7 AND day=28 AND destination_airport_id=(SELECT id FROM airports WHERE city='Fiftyville');
SELECT city FROM airports WHERE id IN (SELECT origin_airport_id FROM flights WHERE year=2023 AND month=7 AND day=28 AND destination_airport_id=(SELECT id FROM airports WHERE city='Fiftyville'));
SELECT * FROM passengers WHERE flight_id=22;
SELECT * FROM flights WHERE passport_number=5773159633 OR passport_number=1695452385;

airports              crime_scene_reports   people
atm_transactions      flights               phone_calls
bakery_security_logs  interviews
bank_accounts         passengers

10:15

| 22 | 1                 | 8                      | 2023 | 7     | 28  | 12   | 51     |

| 260 | 2023 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2023 | 7     | 28  | 10   | 18     | exit     | 94KL13X   *** | 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |!!!!!!!!
| 262 | 2023 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2023 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2023 | 7     | 28  | 10   | 20     | exit     | G412CB7   *** | 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |


| 266 | 2023 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |3592750733
| 267 | 2023 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |8294398571
| 265 | 2023 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |

+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2023 | 7     | 28  | 51       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2023 | 7     | 28  | 36       |
| 233 | (367) 555-5533 | (375) 555-8161 | 2023 | 7     | 28  | 45       |!!!!!
| 251 | (499) 555-9472 | (717) 555-1342 | 2023 | 7     | 28  | 50       |
| 254 | (286) 555-6063 | (676) 555-6554 | 2023 | 7     | 28  | 43       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2023 | 7     | 28  | 49       |
| 261 | (031) 555-6622 | (910) 555-3251 | 2023 | 7     | 28  | 38       |
| 279 | (826) 555-1652 | (066) 555-9701 | 2023 | 7     | 28  | 55       |
| 281 | (338) 555-6650 | (704) 555-2131 | 2023 | 7     | 28  | 54       |
+-----+----------------+----------------+------+-------+-----+----------+

+---------------+
|     city      |
+---------------+
| Chicago       |
| Beijing       |
| Los Angeles   |
| New York City |
| Dallas        |
| Boston        |
| Dubai         |
+---------------+


+--------+---------+----------------+-----------------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate |
+--------+---------+----------------+-----------------+---------------+
| 395717 | Kenny   | (826) 555-1652 | 9878712108      | 30G67EN       |
| 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
| 438727 | Benista | (338) 555-6650 | 9586786673      | 8X428L0       |
| 449774 | Taylor  | (286) 555-6063 | 1988161715      | 1106N58       |
| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
| 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
| 907148 | Carina  | (031) 555-6622 | 9628244268      | Q12B3Z3       |
+--------+---------+----------------+-----------------+---------------+


| 161 | Ruth    | 2023 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| 162 | Eugene  | 2023 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| 163 | Raymond | 2023 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
