# Motus Healthcare

![Motus Healthcare](static/images/readmebanner.jpg)

## CONTENTS
* [Project Goals](#project-goals)
* [Feature Planning](#feature-planning)
* [User Stories](#user-stories)
* [Design](#design)
* [Features Overview](#features-overview)
* [Testing](#testing)
* [Technologies Used](#technologies-used)
* [Installation & Setup](#installation--setup)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

### Design

* [Colour Scheme](#colour-scheme)
* [Typography](#typography)
* [Wireframes](#wireframes)
* [Database Schema](#database-schema)

## Project Goals

**Motus Healthcare** is designed for patients who have undergone elective surgery and require advice, reassurance, and access to a healthcare professional. At this stage, the platform will focus solely on supporting patients recovering from elective surgery.

It is reported that on average, NHS physiotherapy waiting times in the UK can range from 6 to 18 weeks and may wait several months before their first appointment. This is due to high demand for services, limited NHS resources, referral process delays (due to patients needing to see a GP before referral) and triage prioritisation (People with less critical needs will have longer waiting times).

As a physiotherapist, I recognise a clear need for follow up care once a patient has been discharged from hospital and the sooner they receive support and advice the more favourable the outcome of the surgery and functional outcome.

 Many patients feel anxious or uncertain during the early stages of recovery. This platform aims to provide them with quick and easy access to a physiotherapist, nurse or doctor. These Health Care Professionals (HCPs) can offer guidance, reassurance, and, if necessary, escalate any concerns related to their post-operative health including safe guarding concerns.

## Feature Planning

Below is a table of opportunities for the project, together with a score of their importance level and viability (rated low to high, 1-5). Features that score highly on importance and viability will be features that must be addressed first as part of the MVP. Features that are scored mid range are should have features, which will be added to the project once it has achieved MVP status. Low scored features, are could have features and if not attended to in this development version will be marked to be addressed in a future version.

User roles are included in this project as there are different features of the site dependant on what type of user you are. There are three categories of user for the site: **Guest Users** (those who do not have an account), **Users** (who have signed up and verified their account) and **Admins** (users who have superuser status and are able to perform additional tasks on the site reserved for healthcare professionals, such as managing appointments and responding to patient messages).

| User Type   | Feature                          | Importance | Viability | MVP |
| :---------- | :------------------------------- | :--------: | :-------: | :-: |
| User       | Sign up for an account           |     5      |     5     | MVP |
| User       | Log in to existing account       |     5      |     5     | MVP |
| User        | Email Verification               |     3      |     3     |     |
| User        | Password Recovery                |     3      |     3     |     |
| User        | Account Recovery                 |     3      |     3     |     |
| User        | User Profile Management          |     4      |     5     | MVP |
| User        | Profile Picture Upload           |     3      |     5     |     |
| User        | Surgery Type Information         |     4      |     5     |     |
| User        | Book Appointments                |     5      |     5     | MVP |
| User        | View Appointment Status          |     5      |     5     | MVP |
| User        | Amend Appointments               |     5      |     5     | MVP |
| User        | Cancel Appointments              |     5      |     5     | MVP |
| User        | Visual Calendar View             |     4      |     4     |     |
| User        | Contact Healthcare Professionals |     5      |     5     | MVP |
| User        | Send Messages                    |     5      |     5     | MVP |
| User        | View Message Replies             |     5      |     5     | MVP |
| User        | Submit Testimonials              |     3      |     5     |     |
| User        | Read Other Testimonials          |     3      |     5     |     |
| User        | Delete Own Testimonials          |     3      |     5     |     |
| Admin       | View All Appointments            |     5      |     5     | MVP |
| Admin       | Confirm Appointments             |     5      |     5     | MVP |
| Admin       | Mark Appointments Complete       |     5      |     5     | MVP |
| Admin       | View Unreplied Messages          |     5      |     5     | MVP |
| Admin       | Reply to User Messages           |     5      |     5     | MVP |
| Admin       | Therapist Dashboard               |    5      |     5     | MVP |
| All         | Responsive Navigation            |     5      |     5     | MVP |
| All         | Mobile-Friendly Design           |     5      |     5     | MVP |
| All         | Date/Time Validation             |     5      |     5     |     |
| All         | Past Date Prevention             |     5      |     5     | MVP |

### User Stories

#### **User Stories**

**Project Management Board**: [View the project board on GitHub](https://github.com/users/DavidRC-Projects/projects/3/views/1).

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

#### **Acceptance Criteria and Specific tasks**

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

The following users stories were not developed included Email confirmation, account recovery and marking appointments as complete. This was because the other features were prioritised within the available time and will be implemented in the future.

### Design

#### Colour Scheme
The application uses a purple gradient theme throughout, maintaining visual consistency across all pages. The color palette was carefully selected using Coolers to give a professional appearance:

![Colour Palette](documentation/colours.png)

#### Typography
The application uses Google Fonts **Marvel** and **Montserrat** throughout.

- **Marvel**: Used for headings and brand elements, providing a modern, clean aesthetic that conveys professionalism.
- **Montserrat**: Used for body text and navigation, offering excellent readability across all devices and screen sizes.

These font choices were selected for their clean, contemporary appearance that aligns with my view of a more modern healthcare application.

#### Wireframes
Initial wireframes were created using Figma to plan the user interface:

* **Homepage Wireframe** - Initial design concept for the main booking interface and welcome section.

  ![Homepage Wireframe](documentation/figmahome.png)

* **Calendar Wireframe** - Planning the interactive calendar interface for appointment booking.

  ![Calendar Wireframe](documentation/figmacalendar.png)

* **Contact Page Wireframe** - Design concept for the messaging interface between patients and healthcare professionals.

  ![Contact Wireframe](documentation/figmacontact.png)

* **Sign In Wireframe** - Authentication interface design for user login.

  ![Sign In Wireframe](documentation/figmasignin.png)

#### **Database Schema**

Entity Relationship Diagrams (ERD's)

![Database ERD](documentation/erdimage.png)

**How the Database Schema Works:**

The Motus Healthcare application uses a relational database design with Django's built-in User model as the central entity. Here's how the relationships work:

**Core Relationships:**
- **User ↔ UserProfile (1:1)**: Each user has exactly one profile containing extended information like surgery type and profile picture.
- **User ↔ Appointment (1:Many)**: Each user can book multiple appointments over time.
- **User ↔ Message (1:Many)**: Each user can send multiple messages to healthcare professionals.
- **User ↔ Testimonials (1:Many)**: Each user can write multiple testimonials about their experience.
- **Message ↔ Message (1:Many)**: Self-referential relationship allowing threaded conversations with replies.

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



## Features Overview


Each page of the site shares the following:

* **Motus Logo** - The logo maintains consistency across all pages and helps establish trust with users seeking healthcare services.


  ![Motus Logo](documentation/motuslogo.png)

* **Favicon** - I used [Favicon.io](https://favicon.io/) to create the favicon for the site. This small icon appears in browser tabs, making it easier for users to identify and return to the Motus Healthcare website.


  ![Motus Physio Favicon](documentation/motusfavicon.png)


* **Navbar** - The navbar on the site is split into two sections, the first section contains the Motus Physio logo and navigation links. The second section contains the main site navigation including Home, Profile, Bookings, Testimonials, and Contact. The navbar is fully responsive, and utilises a hamburger menu toggle on mobile screens.

  The navigation links will show a white underline to give the user feedback on what page they are on when interacting with the menu. The navbar adapts to show different options depending on whether a user is logged in or not. The navbar also displays the username on the far right on desktop and tablet views and in the middle for mobile views.

  ![Navbar](documentation/navbar.png)


* **Therapist Navbar** - When healthcare professionals/admin users are logged in, the navbar displays additional options including access to the Therapist Dashboard. The user does not have access to this dashboard option. The testimonials and appointment booking pages are omitted as they are not used by the practitioner.  

  ![Therapist Navbar](documentation/therapistnavbar.png)


* **Footer** - The footer contains information about Motus Physio, including contact details and social media links. The footer is fully responsive and uses the same purple gradient theme as the navbar to maintain visual consistency throughout the site.

    ![Site Footer](documentation/footer.png)


* **Defensive Programming** - This has been implemented throughout the site to ensure security and prevent unauthorised access:

  - `@login_required` decorator applied to all user-specific views (booking, profile and messages).
  - Users are automatically redirected to login page when accessing protected routes.
  - Session-based authentication ensures users remain logged in during their visit.
  - `is_staff` check for therapist dashboard access - only healthcare professionals can access admin features.
  - Django admin panel access restricted to admin/staff users only.
  - User-specific data filtering (`filter(user=request.user)`) ensures users can only access their own appointments and messages.

  **Input Validation:**
  - Form validation checks for required fields before processing.
  - Duplicate appointment prevention by checking existing bookings.
  - Date and time validation to prevent past bookings.
  - CSRF protection on all forms to prevent cross-site request forgery.


### Homepage (index.html)
* **Appointment Booking Form** - The main feature allowing users to book appointments with healthcare professionals. Users can select date, time, appointment type, and add optional notes. The form includes real-time validation and prevents booking past dates or unavailable time slots. This ensures users can only book valid appointments.


  ![Homepage Booking Form](documentation/homebooking.png)


* **Welcome Section** - Displays a welcoming message and brief introduction to Motus Healthcare services. This section helps users understand the service and encourages them with a friendly message.


  ![Homepage Welcome Section](documentation/welcomemessagehome.png)


* **Mobile Homepage** - Responsive design showing how the homepage adapts to mobile devices. This ensures users can access the service easily from their smartphones and tablets.


  ![Mobile Homepage](documentation/bookingmobhome.png)


* **Appointment Success Message** - Confirmation message displayed after successful appointment booking with details and next steps. This provides users with reassurance that their booking has been received.


  ![Appointment Success](documentation/homeappsuccess.png)


### User Profile Page (profile.html)
* **Profile Information Display** - Shows user's personal information including username, email, surgery type, and account creation date. Information is displayed using a card-based layout.


  ![Profile Information Display](documentation/profile.png)


* **Profile Picture Management** - Users can upload, change, or delete their profile picture. The system uses Cloudinary for image storage and provides a default placeholder when no image is uploaded.


  ![Profile Picture Management](documentation/profilepicupdate.png)


* **Mobile Profile View** - Responsive profile page for mobile devices and also responsive to tablet view.


  ![Mobile Profile](documentation/profilemob.png)


* **Surgery Type Selection** - Dropdown menu allowing users to select or input their surgery type and allows insight for the therapist before they have contact.


  ![Surgery Type Selection](documentation/surgerydropdown.png)


* **Surgery Type Success** - Confirmation message displayed after successfully updating surgery type information.


  ![Surgery Type Success](documentation/surgerysuccess.png)


* **Confirmed Appointment Display** - Shows confirmed appointments.


  ![Confirmed Appointment](documentation/confirmedappprofile.png)


### Appointment Booking Page (booking.html)
* **Calendar View** - Interactive calendar showing available and booked time slots. Users can click on dates to see available times. The user can click on dates that are free and will be redirected to the appointment bookings page. If the user selects a booked appointment then a warning message will be displayed as a bootstrap modal 'This day is already booked. Please select a different day'.


  ![Booking Calendar View](documentation/bookingcalendar.png)


* **Mobile Calendar View** - Responsive calendar interface for mobile devices and also tablets.


  ![Mobile Calendar](documentation/calendarmob.png)


* **Booked Appointment Display** - Calendar view showing booked appointments with visual indicators and status information. Booked appointments are highlighted in blue and provide the appointment time. This gives the user visual feedback of when they booked their appointments.


  ![Booked Appointment Calendar](documentation/calendarbookedapp.png)


* **Appointment Booking Form** - Booking form with date picker, time selector, appointment type selection (Initial Consultation/Follow Up), and notes field.


  ![Appointment Booking Form](documentation/appbooking.png)


* **Mobile Booking Form**


  ![Mobile Booking Form](documentation/appbookingmob.png)

### View Bookings Page (view_booking.html)
* **Pending Appointment Display** - Shows appointments with pending status, allowing users to view details and manage their bookings. The admin can confirm appointments using Django administration.


  ![Pending Appointment](documentation/viewbookingpending.png)


* **Edit Appointment Success** - Confirmation message displayed after successfully editing appointment details.


  ![Edit Success](documentation/editappsuccess.png)


### Contact Page (message_practitioner.html)
* **Contact Page** - Main contact interface allowing users to send messages to healthcare professionals with form validation.


  ![Contact Page](documentation/contactpage.png)


* **Message History** - Displays all sent messages and received replies in chronological order. Users can view conversation threads and delete their own messages.


  ![Message History](documentation/yourmessagescontact.png)


* **Message Deletion** - Interface for deleting messages with confirmation to prevent accidental deletion.


  ![Message Deletion](documentation/contactmessagedelete.png)


* **Empty Message History** - Display when no messages have been sent yet. This gives the user feedback that there are no messages.


  ![Empty Messages](documentation/contactnomessage.png)

### Testimonials Page (testimonials.html)
* **Testimonials Page** - Main testimonials interface displaying user testimonials in a card-based layout with username, timestamp, and content.


  ![Testimonials Page](documentation/testimonialpage.png)


* **Add Testimonial Success** - Confirmation message displayed after successfully submitting a testimonial.


  ![Testimonial Success](documentation/testsuccess.png)


* **Delete Testimonial** - Interface for deleting testimonials with confirmation modal to prevent accidental deletion.


  ![Delete Testimonial](documentation/testdelete.png)


### Therapist Dashboard (therapist_dashboard.html)
* **Therapist Dashboard** - Main admin interface showing all patient appointments with user details, appointment information and and status.


  ![Therapist Dashboard](documentation/therapistdashboard.png)


  * **Reply Sent Confirmation** - Confirmation message displayed after successfully replying to a patient message.


  ![Reply Sent](documentation/tdreplysent.png)


* **Message Reply Success** - Confirmation message displayed after successfully sending a reply to a patient message.


  ![Message Reply Success](documentation/contactmessagesuccess.png)


* **Admin Appointment View** - View of Django administration. This shows all appointments with user information, appointment details, and admin controls.


  ![Admin Appointment View](documentation/adminappview.png)


* **Admin User Management** - Interface for managing user accounts and viewing user information.


  ![Admin User Management](documentation/adminusers.png)


### Authentication Pages
* **Login Page** - The login form with username/email and password fields. Includes validation and error message display for failed login attempts.


  ![Login Page](documentation/signinpage.png)


* **Login Success** - Confirmation message displayed after successful login.


  ![Login Success](documentation/signinsuccess.png)


* **Registration Page** - User registration form with username, email, and password fields.


  ![Registration Page](documentation/registerpage.png)


* **Logout Page**


  ![Logout Page](documentation/signoutpage.png)


* **Logout Success** - Confirmation message displayed after successful logout.


  ![Logout Success](documentation/signoutsuccess.png)


### Error Pages
* **404 Error Page** - Custom error page for page not found errors with button to return to homepage.


  ![404 Error Page](documentation/error404.png)


* **500 Error Page** - Custom error page for server errors with button to return to homepage.


  ![500 Error Page](documentation/error500.png)

## Testing

###
I performed manual testing on each page and feature of the app to test its functionality and responsiveness.

### Validation Tools Used
- **Python**: PEP8 compliance with proper formatting and documentation.
- **JavaScript**: JSHint validation with ES6 compatibility.
- **HTML/CSS**: W3C validation for markup and styling.

For detailed testing procedures, results, and validation reports, see [TESTING.md](TESTING.md).

## Technologies Used

### Backend
- **Django 4.2** - Python web framework for rapid development.
- **Python 3.13.2+** - Programming language and version.
- **PostgreSQL** - Relational database for data storage.
- **Django Allauth** - Authentication system for user management.
- **Django Summernote** - Rich text editor for admin interface.

### Frontend
- **HTML5** - Markup language.
- **CSS** - Styling and responsive design.
- **JavaScript (ES6)** - Client-side interactivity.
- **Bootstrap 5** - CSS framework for responsive design.
- **jQuery** - JavaScript library for DOM manipulation.

### External Services and tools
- **Cloudinary** - Cloud storage for user profile pictures.
- **Heroku** - Cloud platform for deployment.
- **GitHub** - Version control and code repository.
- **Image Resizer** [Image Resizer](https://imageresizer.com/) to resize images.
- **Tiny PNG** [TinyPNG](https://tinypng.com/) - To compress images and convert them to png.
- **Slack** - For updates and communication.
- [Canva](https://www.canva.com/) - For custom Motus healthcare logo and README image.

### Development Tools
- **VS Code** - Code editor.
- **Git** - Version control.
- **PEP8** - Python style guide compliance.
- **JSHint** - JavaScript code quality tool.
- **W3C Validator** - HTML/CSS validation.

### Key Packages
- **Django 4.2.23** - Main web framework for building the application.
- **django-allauth** - Authentication system for user registration, login, and social authentication.
- **django-crispy-forms** - Form rendering library for better form styling.
- **crispy-bootstrap5** - Bootstrap 5 template pack for crispy forms.
- **django-summernote** - Rich text editor for admin interface.
- **cloudinary** - Cloud storage service for user profile pictures and media files.
- **dj-database-url** - Database URL configuration for Heroku deployment.
- **gunicorn** - WSGI-compatible web server for production deployment on Heroku.
- **psycopg2** - PostgreSQL adapter for Python, used by Django when connecting to PostgreSQL database.
- **whitenoise** - Static file serving middleware for Django in production environments.

## Installation & Setup

### Prerequisites
- Python 3.13.2
- GitHub account (for repository access)
- A PostgreSQL database
- A Cloudinary account (free tier is fine)

### Local Development Setup

1. **Fork and Clone the Repository**
   - **Fork the Repository:**
     - Go to the original repository on GitHub.
     - Click the "Fork" button in the top-right corner.
     - Select your GitHub account to create a fork.
   
   - **Clone Using VS Code:**
     - Open VS Code.
     - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open Command Palette.
     - Type "Git: Clone" and select it.
     - Enter your forked repository URL: `https://github.com/your-username/motus_physio.git`.
     - Choose a local folder to save the project.
     - Click "Clone".
     - VS Code will automatically open the project folder.

2. **Set Up Virtual Environment**
   - **Create Virtual Environment:**
     - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open Command Palette.
     - Type "Python: Create Environment" and select it.
     - Choose "Venv" as the environment type.
     - Select your Python interpreter (usually the latest version).
     - Choose ".venv" as the environment name.
     - VS Code will create the virtual environment automatically.
   
   - **Verify Virtual Environment:**
     - Check that '.venv' is displayed in the bottom information bar (on the right hand side).

3. **Install Dependencies**
   - **Install from requirements.txt:**
     - Ensure your virtual environment is activated (you should see `(.venv)` in terminal).
     - Run: `pip install -r requirements.txt`.
     - You should see a success message when installation is complete.
   
   - **Verify Installation:**
     - Run: `pip list` to see all installed packages.
     - You should see Django and other packages listed.

4. **Environment Variables**
   - **Create .env File:**
     - In VS Code, right-click in the explorer panel (left sidebar).
     - Select "New File".
     - Name it exactly `.env` (with the dot).
     - Add the following content:

import os
os.environ.setdefault("DATABASE_URL", <database_url_goes_here>)
os.environ.setdefault("SECRET_KEY", <secret_key_goes_here>)
os.environ.setdefault("CLOUDINARY_CLOUD_NAME", <cloud_name_goes_here>)
os.environ.setdefault("CLOUDINARY_API_KEY", <api_key_goes_here>)
os.environ.setdefault("CLOUDINARY_API_SECRET", <api_secret_goes_here>)

5. **Database Setup**
   - **Run Migrations:**
     - Open VS Code terminal (ensure virtual environment is activated).
     - Run: `python manage.py migrate`.
     - Wait for all migrations to complete.

6. **Create Superuser**
   - **Set Up Admin Account:**
     - In the terminal, run: `python manage.py createsuperuser`.
     - Enter a username when prompted.
     - Enter an email address when prompted.
     - Enter and confirm a password when prompted.

7. **Collect Static Files**
   - **Prepare Static Files:**
     - In the terminal, run: `python manage.py collectstatic`.
     - Type "yes" when prompted to collect static files.
     - Files will be copied to the `staticfiles` directory.

8. **Run Development Server**
   - **Start Local Server:**
     - In the terminal, run: `python manage.py runserver`.
     - You should see "Starting development server at http://127.0.0.1:8000/".
     - Open your web browser and go to `http://127.0.0.1:8000/`.
     - Your app should now be running locally.

- **Cloudinary Setup**: Sign up for a free account at [cloudinary.com](https://cloudinary.com) and get your cloud name, API key, and API secret
- **Database**: For local development, you can use SQLite (Django's default) or set up PostgreSQL
- **Static Files**: The project uses Django's static file handling with Cloudinary for media files

## Deployment

This project is deployed on [Heroku](https://www.heroku.com/). Follow these steps to deploy your own instance:

### 1. Prepare for Deployment

**Install Required Packages:**
- Open VS Code terminal (ensure virtual environment is activated).
- Run: `pip install whitenoise gunicorn`.
- Run: `pip freeze --local > requirements.txt`.
- This updates your requirements.txt with the new packages.

**Create Procfile:**
- In VS Code, right-click in the explorer panel (left sidebar).
- Select "New File".
- Name it exactly `Procfile` (no file extension).
- Add this content: `web: gunicorn my_project.wsgi`.
- Save the file.

**Update Settings.py:**
- Open `my_project/settings.py` in VS Code.
- Find the `ALLOWED_HOSTS` setting and update it to: `ALLOWED_HOSTS = [".herokuapp.com"]`.
- Add this line: `CSRF_TRUSTED_ORIGINS = ["https://*.herokuapp.com"]`.
- Find `DEBUG = True` and change it to: `DEBUG = False`.
- Save the file.

### 2. Heroku Setup

**Create Heroku Account:**
- Go to [heroku.com](https://www.heroku.com/).
- Click "Sign up" and create a new account.
- Verify your email address.

**Create New App:**
- Go to your Heroku dashboard.
- Click "New" → "Create new app".
- Enter a unique app name.
- Select "Common Runtime Europe" for location.
- Click "Create app".

**Connect GitHub Repository:**
- In your Heroku app dashboard, go to "Deploy" tab.
- Under "Deployment method", select "GitHub".
- Click "Connect to GitHub".
- Authorize Heroku to access your GitHub account.
- Search for your repository and click "Connect".

### 3. Configure Environment Variables

**Get Your Values Ready:**
- **SECRET_KEY**: Generate a new Django secret key or use your existing one.
- **Cloudinary Credentials**: Get these from your Cloudinary dashboard.

**Add Environment Variables:**
- In Heroku dashboard, go to "Settings" tab.
- Scroll down to "Config Vars" section.
- Click "Reveal Config Vars".
- Add each variable one by one:
  - `DATABASE_URL`: Provided by PostgreSQL.
  - `SECRET_KEY`: Your Django secret key.
  - `CLOUDINARY_CLOUD_NAME`: Your Cloudinary cloud name.
  - `CLOUDINARY_API_KEY`: Your Cloudinary API key.
  - `CLOUDINARY_API_SECRET`: Your Cloudinary API secret

### 4. Deployment

**Deploy from GitHub:**
- In "Deploy" tab, scroll down to "Manual deploy" section.
- Select the main branch.
- Click "Deploy Branch".

Heroku deployment link: https://motus-physio-2117024da225.herokuapp.com/

## Credits

### Data Sources
- **[NHS Physiotherapy Waiting Times Data](https://flexcareinjuryclinic.co.uk/nhs-physiotherapy-waiting-list-sheffield)** - Information about NHS physiotherapy waiting times in the UK.

### Design Resources
- **[Canvas](https://canvas.com)** - Logo design, README banner image and flow diagram for ERD.
- **[Pexels](https://pexels.com)** - User profile photos for testing and application use.
- **[Coolors](https://coolors.co)** - Color palette generation and selection.
- **[jQuery Timepicker](https://timepicker.co)** - Time selection plugin for appointment booking.
- **[Favicon.io](https://favicon.io/favicon-converter/)** - Favicon generation and conversion.

### Learning Resources
- **[Django Project](https://www.djangoproject.com/)** - Official Django documentation and framework.
- **[CodeStars Blog](https://learn.codeinstitute.net/)** - Django tutorial by code institute.
- **[Think Therefore I Blog](https://learn.codeinstitute.net/)** - Django tutorial by code institute.

### Video Tutorials
- **[Django Walkthrough Tutorial](https://www.youtube.com/watch?v=l0QEGvAX8rU)** - Django guide.
- **[Django Models Tutorial](https://www.youtube.com/watch?v=48KzlkIqOnM)** - Understanding Django models and database relationships.

## Acknowledgements
* I would like thank my mentor Jubril Akolade for his advice and support during the project. Jubril helped give advice on improving the user experience by adding an image in the user icon and adding bootstrap model alerts.
* I would like to thank my partner and family for their unwavering support during this project.

[Back to Contents](#contents)