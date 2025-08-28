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

| User Type   | Feature                          | Importance | Viability | MVP |
| :---------- | :------------------------------- | :--------: | :-------: | :-: |
| User       | Sign up for an account           |     5      |     5     | MVP |
| User       | Log in to existing account       |     5      |     5     | MVP |
| User        | Email Verification               |     3      |     3     |   |
| User        | Password Recovery                |     3      |     3     |   |
| User        | Account Recovery                 |     3      |     3     |   |
| User        | User Profile Management          |     4      |     5     | MVP |
| User        | Profile Picture Upload           |     3      |     5     | MVP |
| User        | Surgery Type Information         |     4      |     5     | MVP |
| User        | Book Appointments                |     5      |     5     | MVP |
| User        | View Appointment Status          |     5      |     5     | MVP |
| User        | Amend Appointments               |     5      |     5     | MVP |
| User        | Cancel Appointments              |     5      |     5     | MVP |
| User        | Visual Calendar View             |     4      |     4     | MVP |
| User        | Contact Healthcare Professionals |     5      |     5     | MVP |
| User        | Send Messages                    |     5      |     5     | MVP |
| User        | View Message Replies             |     5      |     5     | MVP |
| User        | Submit Testimonials              |     3      |     5     | MVP |
| User        | Read Other Testimonials          |     3      |     5     | MVP |
| User        | Delete Own Testimonials          |     3      |     5     | MVP |
| Admin       | View All Appointments            |     5      |     5     | MVP |
| Admin       | Confirm Appointments             |     5      |     5     | MVP |
| Admin       | Mark Appointments Complete       |     5      |     5     | MVP |
| Admin       | View Unreplied Messages          |     5      |     5     | MVP |
| Admin       | Reply to User Messages           |     5      |     5     | MVP |
| Admin       | Therapist Dashboard               |     5      |     5     | MVP |
| All         | Responsive Navigation            |     5      |     5     | MVP |
| All         | Mobile-Friendly Design           |     5      |     5     | MVP |
| All         | Date/Time Validation             |     5      |     5     | MVP |
| All         | Past Date Prevention             |     5      |     5     | MVP |

### User Stories

#### **User Stories**

| User Story ID | As a/an | I want to be able to ... | So that I can... |
| :--- | :--- | :--- | :---|
| Navigation bar | user | view and interact with the navigation bar | I can easily access different parts of the website from any page |
| User login and logout | user | securely log in and log out of the application | I can access my account and protect my data|
| Register an account | user | register an account | securely log in and book my appointment |
| Profile view | user | view and edit my profile details | manage my personal data |
| Book an appointment | user | book an appointment | speak to a HCP |
| View appointment status | user | see the status of each appointment | know if an appointment has been booked |
| Amend an appointment | user | change the time of the appointment | have flexibility when booking|
| Contact | user | send messages to healthcare professionals | get advice and support about my post-operative recovery |
| Testimonials | user | share my recovery experience and read others' stories | help other users and build trust in the service |
| View appointments | Admin | see all patient appointments in the system | manage the appointment schedule |
| View messages | Admin | see all patient messages that need responses | provide timely support and advice to users |
| Reply to messages | Admin | respond to patient messages and concerns | users get a bespoke response from the therapist in a timely manner |
| Appointment marked as confirmed | Admin | approve and confirm patient appointments | ensure users know their appointments are confirmed |
| Appointment marked as complete | Admin | mark appointments as finished | track user care progress and maintain records |

#### **Acceptance Criteria**

**Navigation bar**
1. The navbar should be visible on all pages.
2. There should be clearly labeled links (Home, Profile, Bookings, Register and Logout).
3. The active page should be highlighted.
4. The navbar should adapt for logged-in and logged-out users:
-shows login/register if not authenticated.
-shows logout/profile and bookings if authenticated.
5. The navbar should be responsive to different devices with a drop down for smaller screens.
6. Clicking the navbar links should take the user to the correct page.

**Login and logout**
1. The user can login to their account using username/email and password.
2. When logged in the user should be redirected to the homepage.
3. When logged in the login and register page should not be visible and replaced with logout.
4. There should be feedback that I am logged in with my name displayed in the navbar.
5. The user can log out of the account securely.
6. After logout, the user should be redirected to the homepage.
7. Login form should validate required fields and show appropriate error messages.
8. Failed login attempts should show clear error messages without revealing sensitive information.

**Register an account**
1. The user can register an account with username, email, and password.
2. Account should be created when valid details are added.
3. Error message should be sent for duplicate email addresses.
4. Should prompt user with an error message when the user enters blank fields.
5. The user should have feedback that the account has been registered successfully.
6. Password should meet minimum security requirements.
7. Username should be unique across the system.
8. Email should be in valid format and unique.
9. User should be automatically logged in after successful registration.
10. UserProfile should be automatically created upon registration.

**Profile View**
1. Display data including name, email, profile picture, type of surgery and account creation date.
2. Details can be saved and updated in real-time.
3. Displays an error if request fails.
4. If I'm not logged in then it should redirect me back to the login page.
5. A picture can be uploaded.
6. The user can change their photo by uploading a new one.
7. The user can delete their photo and return to default placeholder.
8. Gives feedback when the user makes a change with success messages.
9. Surgery type field should allow free text input for various surgery types.
10. Profile should be accessible only to the logged-in user.

**Book an Appointment**
1. Booking page should have a date/time selection and submit button.
2. Times that are already selected should show an error message when the user attempts to book.
3. Successful booking should show a confirmation message and appointment status set to pending.
4. The user can only input times in 30 minute increments.
5. Times can only be from 9am to 9pm, available all days of the week.
6. The user will see all appointments on a visual calendar.
7. The user should be prevented from selecting past dates.
8. Appointment type selection should include Initial Consultation and Follow Up options.
9. Notes field should be optional for additional information.
10. Form validation should check all required fields before submission.
11. User should be redirected to their profile after successful booking.
12. Calendar should update immediately to show the new booking.


**View Appointment Status**
1. The list of appointments should display current status (Pending, Confirmed, Completed).
2. Each appointment should show date, time, type, and current status clearly.
3. Status should be colour-coded for easy identification (e.g., Pending=Yellow, Confirmed=Green, Completed=Blue).
4. Appointment details should include notes and creation timestamp.
5. Calendar view should show appointment status.

**Amend an Appointment**
1. I should be able to update the time/date through an edit form.
2. The updated appointment should retain pending status with new time/date.
3. I should receive feedback if I book/amend.
4. The amended booking should appear in the upcoming bookings on the dashboard and remove the old booking.
5. Validation should prevent booking in the past or on unavailable dates.
6. User should receive confirmation when appointment is successfully amended.
7. Calendar should update immediately to reflect the change.
8. Original appointment should be completely replaced, not duplicated.
9. Edit should maintain the same appointment ID.

**Cancel an Appointment**
1. User profile should show list of upcoming appointments.
2. Appointments can be cancelled by the user or changed to another date.
3. When appointment cancelled it should no longer appear in the upcoming appointments list.
4. The user should get feedback when an appointment is cancelled.
5. The visual calendar will update the changes of any cancellation.
6. Cancel action should require user confirmation to prevent accidental cancellations.
7. Cancelled appointments should be removed from the system completely.

**Contact**
1. Users can send messages to healthcare professionals through a contact form.
2. The contact form should include subject and message fields.
3. Users can view their own sent messages and any replies received.
4. Users can delete their own messages and replies.
5. Messages are displayed in chronological order with timestamps.
6. Users receive confirmation when messages are sent successfully.
7. The contact page should be accessible from the navigation menu.
8. Users must be logged in to send messages.

**Testimonials**
1. Users can submit their own testimonials about their recovery experience.
2. Testimonials should include a text area for the testimonial content.
3. Users can view all testimonials from other patients.
4. Users can delete their own testimonials.
5. Testimonials should display the username and timestamp.
6. Users must be logged in to submit testimonials.
7. The testimonials page should be accessible from the navigation menu.

**Admin - View Appointments**
1. Admin users can see all patient appointments in the system.
2. Appointments should display user details, date, time, type, and status.
3. Appointments should be sorted by date and time.
4. Admin can filter appointments by status (pending, confirmed, completed).
5. Admin can search appointments by patient name or date.
6. The admin dashboard should be accessible only to staff users.
7. Appointments should show creation and update timestamps.

**Admin - View Messages**
1. Admin users can see all patient messages that need responses.
2. Messages should display sender details, subject, content, and timestamp.
3. Only unreplied messages should be visible in the dashboard.
4. Messages should be sorted by creation date.
5. Messages that have been replied to should be hidden from the dashboard.

**Admin - Reply to Messages**
1. Admin users can respond to patient messages through a reply form.
2. Reply form should include a text input field for the response.
3. When a reply is sent, the original message should be marked as replied to.
4. Replies should be linked to their parent messages for conversation threading.
5. Admin should receive confirmation when replies are sent successfully.
6. After replying, messages should no longer appear in the "needs reply" dashboard.
7. Reply timestamps should be recorded for tracking response times.

**Admin - Mark Appointment as confirmed**
1. Admin can change appointment status from pending to confirmed.
2. Status changes should be reflected immediately in the user dashboard.
3. Admin can only modify appointment status.

**Admin - Mark Appointment as complete**
1. Admin can mark appointments as completed after they finish.
2. Status changes should be reflected immediately in the user dashboard.
3. Admin can only modify appointment status.

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



## General Features of the Site

Each page of the site shares the following:

* **Favicon** - I used [Favicon.io](https://favicon.io/) to create the favicon for the site.

  ![Motus Physio Favicon](static/images/motusfavicon.png)

* **Navbar** - The navbar on the site is split into two sections, the first section contains the Motus Physio logo and navigation links. The second section contains the main site navigation including Home, Profile, Bookings, Testimonials, and Contact. The navbar is fully responsive, and utilises a hamburger menu toggle on smaller screens.

  The navigation links have smooth transitions and hover effects that give the user additional feedback when interacting with the menu. The navbar adapts to show different options depending on whether a user is logged in or not.

  ![Large Navbar](static/images/motusnavbar.png)

* **Footer** - The footer contains information about Motus Physio, including contact details and social media links. The footer is fully responsive and uses the same purple gradient theme as the navbar to maintain visual consistency throughout the site.

  ![Site Footer](static/images/motusfooter.png)






https://flexcareinjuryclinic.co.uk/nhs-physiotherapy-waiting-list-sheffield
