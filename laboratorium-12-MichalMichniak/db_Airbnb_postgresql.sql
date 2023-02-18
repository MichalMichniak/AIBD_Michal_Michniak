CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "email" varchar UNIQUE
);

CREATE TABLE "bookings" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "place_id" integer,
  "start_date" date,
  "end_date" date,
  "price_per_night" float,
  "num_nights" integer
);

CREATE TABLE "places" (
  "id" integer PRIMARY KEY,
  "host_id" integer UNIQUE NOT NULL,
  "address" varchar,
  "city_id" integer
);

CREATE TABLE "reviews" (
  "id" integer PRIMARY KEY,
  "booking_id" integer,
  "rating" tinyint,
  "review_body" text
);

CREATE TABLE "hosts" (
  "id" integer PRIMARY KEY,
  "user_id" integer
);

CREATE TABLE "cities" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "country_id" integer
);

CREATE TABLE "countries" (
  "id" integer PRIMARY KEY,
  "country_code" varchar,
  "name" varchar
);

ALTER TABLE "cities" ADD FOREIGN KEY ("country_id") REFERENCES "countries" ("id");

ALTER TABLE "places" ADD FOREIGN KEY ("host_id") REFERENCES "hosts" ("id");

ALTER TABLE "bookings" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "bookings" ADD FOREIGN KEY ("place_id") REFERENCES "places" ("id");

ALTER TABLE "places" ADD FOREIGN KEY ("city_id") REFERENCES "cities" ("id");

ALTER TABLE "hosts" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("booking_id") REFERENCES "bookings" ("id");
