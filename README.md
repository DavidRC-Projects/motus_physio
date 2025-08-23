# Motus Healthcare

![Motus Healthcare](static/images/readmebanner.jpg)



## CONTENTS
* [Project Goals](#project-goals)
* [Feature Planning](#feature-planning)
* [User Stories](#user-stories)


### Design

* [Database Schema](#database-schema)
* [Colour Scheme](#colour-scheme)
* [Typography](#typography)
* [Wireframes](#wireframes)


## Project Goals

**Motus Healthcare** is designed for patients who have undergone elective surgery and require advice, reassurance, and access to a healthcare professional. At this stage, the platform will focus solely on supporting patients recovering from elective surgery.

It is reported that on average, NHS physiotherapy waiting times in the UK can range from 6 to 18 weeks and may wait several months before their first appointment. This is due to high demand for services, limited NHS resources, referral process delays (due to patients needing to see a GP before referral) and triage prioritisation (People with less critical needs will have longer waiting times).

As a physiotherapist, I recognise a clear need for follow up care once a patient has been discharged from hospital and the sooner they receive support and advice the more favourable the outcome of the surgery and functional outcome.

 Many patients feel anxious or uncertain during the early stages of recovery. This platform aims to provide them with quick and easy access to a physiotherapist, nurse or doctor. These Health Care Professionals (HCPs) can offer guidance, reassurance, and, if necessary, escalate any concerns related to their post-operative health including safe guarding concerns.

## Feature Planning

 |User Type | Feature | Importance | Viability |  | Delivered |
| :--- | :--- | :---: | :---: | :---: | :---: |

### User Stories

#### **User Stories**

| User Story ID | As a/an | I want to be able to ... | So that I can... |
| :--- | :--- | :--- | :---|
| Navigation bar | user | view and interact with the navigation bar | I can easily access different parts of the website from any page |
| User login and logout | user | securely log in and log out of the application | I can access my account and protect my data|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|
| :--- | :--- | :--- | :---|

Acceptance Criteria
Navigation bar
1. The navbar should be visible on all pages.
2. There should be clearly labeled links (Home, Profile, Bookings, Register and Logout).
3. The active page should be highlighted.
4. The navbar should adapt for logged-in and logged-out users:
-shows login/register if not authenticated.
-shows logout/profile and bookings if authenticated.
5. The navbar should be responsive to different devices with a drop down for smaller screens.
6. Clicking the navbar links should take the user to the correct page.

Login and logout
1. The user can login to their account.
2. When logged in the user should be redirected to the homepage.
3. When logged in the login and register page should not be visible and replaced with 4. logout.
5. There should be feedback that i am logged in with my name.
6. The user can log out of the account.

#### **Database Schema**

Entity Relationship Diagrams (ERD's)

| Model        | Key | Name              | Type              | Description |
| :----------- | :-- | :---------------- | :---------------- | :---------- |
| **User**     | PK  | id                | AutoField         | Django's built-in authentication model that handles user accounts, login/logout, and permissions. Each user can have one profile and multiple appointments, messages, and testimonials. |
| User         |     | username          | CharField         | Unique identifier for login and display purposes. Must be unique across all users in the system. |
| User         |     | email             | EmailField        | User's primary contact method and in future for account verification. |
| User         |     | password          | CharField         | Securely hashed password for authentication. |
| User         |     | is_staff          | BooleanField      | Flag that grants access to admin panel and therapist dashboard. Healthcare professionals/admin have this set to True. |
| **UserProfile** | PK  | id                | AutoField         | Unique identifier for each user's extended profile information. Automatically created when a user registers. |
| UserProfile  | FK  | user              | OneToOneField     | Direct link to the User model. Each user has exactly one profile, creating a one-to-one relationship. |
| UserProfile  |     | profile_picture   | CloudinaryField   | User's profile image stored in Cloudinary cloud service. Includes default placeholder image for users without photos. |
| UserProfile  |     | surgery_type      | CharField(100)    | Records the specific type of elective surgery the patient underwent (e.g., knee replacement, hip surgery). Helps healthcare professionals provide targeted advice. |
| UserProfile  |     | created_at        | DateTimeField     | Timestamp when the profile was first created |
| UserProfile  |     | updated_on        | DateTimeField     | Timestamp of the last profile modification |
| **Appointment** | PK  | id                | AutoField         | Unique identifier for each appointment booking. Used for tracking, editing, and administrative purposes. |
| Appointment  | FK  | user              | ForeignKey        | Links each appointment to the user who booked it. Allows users to have multiple appointments over time. |
| Appointment  |     | appointment_date  | DateField         | The scheduled date for the appointment. Users cannot book appointments in the past due to validation. |
| Appointment  |     | appointment_time  | TimeField         | The specific time slot for the appointment. Healthcare professionals are available Monday to Friday, 9am to 9pm. |
| Appointment  |     | appointment_type  | CharField(100)    | Categorises appointments as either 'Initial Consultation' (first visit) or 'Follow Up' (subsequent visits). |
| Appointment  |     | notes             | TextField         | Optional additional information from the patient about their condition, concerns, or specific questions for the healthcare professional. |
| Appointment  |     | status            | CharField(20)     | Tracks appointment lifecycle: 'Pending' (awaiting confirmation), 'Confirmed' (approved by healthcare professional), 'Completed' (appointment finished). |
| Appointment  |     | created_at        | DateTimeField     | Timestamp when the appointment was first booked by the user. |
| Appointment  |     | updated_at        | DateTimeField     | Timestamp of the last status change or modification to the appointment. |
| **Message**  | PK  | id                | AutoField         | Unique identifier for each message in the communication system. Enables tracking and management of patient-practitioner conversations. |
| Message      | FK  | user              | ForeignKey        | Links each message to the user who sent it. Users can send multiple messages to healthcare professionals. |
| Message      |     | subject           | CharField(150)    | Brief description of the message topic. Helps organise conversations and makes it easier for healthcare professionals to prioritise responses. |
| Message      |     | message           | TextField         | The main content of the message. Patients can describe symptoms, ask questions, or request advice about their post-operative recovery. |
| Message      |     | reply             | BooleanField      | Flag indicating whether this message is a response from a healthcare professional (True) or an original patient message (False). |
| Message      | FK  | parent_message    | ForeignKey        | Self-referential field that links replies to their original messages. Creates threaded conversations and allows healthcare professionals to respond to specific patient concerns. |
| Message      |     | created_at        | DateTimeField     | Timestamp when the message was sent. Used for conversation history and response time tracking. |
| **Testimonials** | PK  | id                | AutoField         | Unique identifier for each testimonial. Enables users to share their recovery experiences and helps build trust with potential patients. |
| Testimonials | FK  | user              | ForeignKey        | Links each testimonial to the user who wrote it. Users can post multiple testimonials about different aspects of their recovery journey. |
| Testimonials |     | testimonial       | TextField         | The user's personal account of their experience with Motus Healthcare. |
| Testimonials |     | created_at        | DateTimeField     | Timestamp when the testimonial was first posted. |
| Testimonials |     | updated_at        | DateTimeField     | Timestamp of the last modification to the testimonial. |



https://flexcareinjuryclinic.co.uk/nhs-physiotherapy-waiting-list-sheffield

