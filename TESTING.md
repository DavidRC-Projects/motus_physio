# Manual Testing

## User Authentication Testing

### Registration Validation
| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Username Length (Valid) | Entered username "user23" | Username accepted and prompted for password | Pass |
| Duplicate Username | Tried to create account with existing username "user22" | Error: "A user with that username already exists" | Pass |
| Duplicate Email | Tried to register with existing email from user22 | Error: "A user is already registered with this email address" | Pass |
| Password Too Common | Used football team name as password | Error: "This password is too common" | Pass |
| Password Similar to Username | Used same password as username | Error: "The password is too similar to the username" | Pass |
| Password Too Short | Used password shorter than 8 characters | Error: "This password must contain at least 8 characters" | Pass |
| Valid Password | Entered password "password123" during registration | Password accepted | Pass |
| Email Mismatch | Entered different emails in both fields | Error: "You must type the same email each time" | Pass |
| Missing Second Email | Left second email field empty | Error: "Please fill in this field" | Pass |
| Incomplete Email | Entered "user23@" without domain | Error: "Please enter a part following '@'. 'email' is incomplete" | Pass |
| Successful Registration | Completed valid registration | Success message: "Successfully signed in" | Pass |

### Login Validation
| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Valid Credentials | Entered existing username and password | Successfully logged in | Pass |
| Invalid Username | Entered non-existent username | Error message: "Incorrect username or password" | Pass |
| Invalid Password | Entered incorrect password for existing user | Error message: "Incorrect username or password" | Pass |
| Missing Fields | Submitted form with empty username/password | Form validation prevented submission | Pass |

### Authentication Flow
| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Protected Route Access - Profile | Try to access profile page without login | Redirected to login page | Pass |
| Protected Route Access - Appointments | Try to access book appointment page without login | Redirected to login page | Pass |
| Protected Route Access - View Bookings | Try to access viewbooking page without login | Type Error at /view-booking/ | Fail |
| Protected Route Access - Contact | Try to access contact page without login | Redirected to login page | Pass |
| Public Route Access - Testimonials | Try to access testimonials page without login | Testimonial page shown | Pass |
| Protected Route Access - Appointments Dropdown | Try to access appointment dropdown without login | Redirected to login page | Pass |
| Post-Login Redirect | Check redirect after successful login | Redirected to appropriate page | |
| Logout Functionality | Click logout button/link | Successfully logged out | |
| Post-Logout Redirect | Check redirect after logout | Redirected to sign in  page | |


## Base Template Testing

### Navigation Bar Testing
| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Logo Display | Check if Motus logo appears correctly | Logo displays as circular image with text | Pass |
| Brand Text | Verify "MOTUS Healthcare" text | Brand text displays correctly | Pass |
| Fixed Positioning | Check if navbar stays at top when scrolling | Navbar remains fixed at top of viewport |Pass |
| Responsive Toggle | Test burger menu on mobile devices | Burger menu functions on mobile device | Pass |
| Active State Highlighting | Check if current page is highlighted | Current page navigation link not showing active state | Fail |
| Dropdown Functionality | Test Appointments dropdown menu | Dropdown opens and shows Book/View options | Pass |
| Authentication Links | Check Register/Login links when logged out | Authentication links display correctly | Pass |
| Logout Link | Verify logout link when logged in | Logout link appears for authenticated users | Pass |




## Bug fixes and testing after fix
| Protected Route Access - View Bookings | Try to access viewbooking page without login | Type Error at /view-booking/ | Pass |

Fix:
When logged out i clicked on the view-bookings page and it came up with the following error: TypeError at /view-booking/
Field 'id' expected a number but got <SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x107d73980>>.

This was fixed by adding @login required for the booking_calendar_view function in the views.py.

| Active State Highlighting | Check if current page is highlighted | Current page navigation showing active state | Pass |
No CSS styles applied for active nav bar link. Added this to underline in white when page is active.