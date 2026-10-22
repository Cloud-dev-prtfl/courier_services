**Date:** 5/10/2025
**Company:** A. Centauri Software

# Courier Services: Requirements Document
**Project:** Creative Delivery Web Application Platform  
**Version:** 1.0  
**Date:** October 05, 2025  

## Introduction
This document provides a concise, high-level summary of the essential, user-facing features and strategic requirements for the Online Delivery Web Application, derived from the detailed technical specification. This overview is intended for quick comprehension of the application's scope and primary objectives.

This summary serves as a stakeholder communication tool, focusing on the "what" and "why" rather than the implementation "how." It is designed to facilitate project alignment among product owners, management, and other non-technical teams. All functional requirements outlined here are based strictly on publicly visible user interfaces and advertised capabilities. References to internal systems, databases, or specific APIs have been intentionally omitted to maintain a high-level perspective. The successful delivery of these features will ensure a seamless and intuitive user experience across all supported platforms.

## Table of Contents

| Section | Title | Page |
| :--- | :--- | :--- |
| 1.0 | Introduction | 1 |
| 2.0 | Table of Contents | 2 |
| 3.0 | Functional Requirements | 2 |
| 3.1 | User Authentication and Profile Management | 2 |
| 3.2 | Delivery Order Initiation and Service Selection | 3 |
| 3.3 | Real-Time Order Tracking | 5 |
| 3.4 | Location and Region Management | 5 |
| 3.5 | Information and Support Access | 6 |
| 3.6 | Partner/Courier Onboarding Interface | 6 |
| 3.7 | Business Sales Inquiry Interface | 6 |
| 4.0 | Non-Functional Requirements (NFR) | 7 |
| 4.1 | Performance and Usability | 7 |
| 4.2 | Security and Service Assurance | 7 |
| 4.3 | Compliance and Extensibility | 7 |
| 5.0 | Conclusion | 8 |

## 3.0 Functional Requirements
The following requirements define the core functions the system must perform to satisfy the needs of its users.

### 3.1 User Authentication and Profile Management
**Description:** The system must provide secure and reliable entry points for users to manage session and identity.

* **3.1.1 Log In:** The system shall provide a secure log-in module accepting valid user credentials (email/phone and password) and validating them against the registered user base.
    * **Credential Validation:** The log-in module shall perform client-side validation for phone number/email format before enabling submission. The email format must pass standard regex validation. Phone number input must enforce a 10-digit numeric format for the Indian market.
    * **Error Handling:** The system shall display a concise and descriptive error message on the screen for invalid credentials or connection failures. Error messages must appear inline, immediately below the field where the error occurred, without closing the login module.
    * **Success Redirect:** Upon successful login, the user shall be redirected to the main Dashboard (e.g., `/dashboard`) which presents active and past orders, or to the last booking page they accessed if a session was incomplete. If the login occurs via a modal, the modal shall close, and the page shall refresh to reflect the authenticated user state (e.g., showing 'My Account' instead of 'Log in'). The page refresh shall include a loading spinner overlaying the content until user data (e.g., name, current orders) is fully fetched and displayed, ensuring no Cumulative Layout Shift (CLS).
* **Sign Up:** The system shall provide a registration workflow that captures mandatory user contact details (name, contact number, email) and requires the creation of a secure password.
    * **Password Policy:** The registration workflow shall enforce a minimum password length of 8 characters and require a mix of uppercase, lowercase, and numeric characters. The system must provide real-time password strength feedback (e.g., Weak, Medium, Strong) as the user types.

### 3.2 Delivery Order Initiation and Service Selection
**Description:** The system must enable users to initiate and specify parameters for a new delivery booking through a guided, multi-step workflow.

* **3.2.1 Booking CTA:** The application shall prominently display a primary Call-to-Action (CTA) (e.g., "Order delivery," "Get delivery now") that redirects the user to the parcel booking workflow upon click or tap.
    * **Redirection/Modal:** The CTA shall either redirect the user to a dedicated multi-step booking page (e.g., `/booking/start`) OR initiate an inline booking modal that overlays the current page content. This modal must be dismissible by the user via a 'close' icon (X) or the ESC key and must maintain its state if dismissed and reopened. This modal shall be implemented with a high z-index (e.g., 1000), prevent background scrolling, and include an accessibility trap to keep keyboard focus within the modal boundaries. The modal title must be "Start Your Delivery."
    * **Service Categorization:** The system shall present distinct, selectable options for all advertised service types (e.g., Scheduled, Next Day, Same Day, Express, Instant) during the booking process.
    * **Service Detail Display:** For each service type, the system shall display a concise tooltip or description detailing the estimated delivery time frame and associated base rate. This information must be sourced dynamically based on the user's selected region (4.1). When selected, the corresponding option must be visually highlighted (e.g., using a border and background color change).
    * **Cost Calculation Trigger:** Selection of a service type shall immediately recalculate the delivery estimate once all address and package parameters are defined. The displayed cost estimate must dynamically update within 500ms of any change to address, weight, dimensions, or service type. A brief "Calculating..." state must be displayed during the API call.
    * **Item Type Input:** The system shall require the user to categorize the item being delivered using a predefined list to ensure appropriate handling and courier matching.
    * **Predefined List:** The Item Type selection shall be presented as a radio button group or dropdown containing the specific categories (Food & Groceries, Pharmaceuticals, E-commerce & retail, Electronics, Office supplies, Flowers & gifts). Selecting a prohibited category (if applicable) must trigger an immediate user notification, blocking progress until the selection is changed. The notification must be a persistent warning banner at the top of the booking module.
    * **Price and Detail Input:** The application shall clearly display the starting price for available services (e.g., "from ₹ 45") in a location immediately proximate to the main booking CTA and guide the user through mandatory input steps.
    * **Mandatory Address Input:** The booking workflow shall require the user to input a Pickup Address and a Drop-off Address. The input fields must utilize a geo-location service API for address auto-completion, providing suggestions after the third character input. The selected address must store Latitude and Longitude coordinates. Address objects retrieved from the geo-location service shall be stored with keys: `address_line_1`, `city`, `state`, `pin code`, and mandatory `latitude`/`longitude` (Float 64 format).
    * **Package Parameter Input:** The booking workflow shall include mandatory input fields for Package Weight (in kg, minimum value 0.1, max 25), and Package Dimensions (Length x Width x Height in cm, minimum 1 cm for each). These fields must use numerical input types with client-side validation for positive values. An icon indicating weight/size restrictions must be displayed next to the input fields. If the max value (25kg) is exceeded, a specific error message "Weight exceeds standard courier limit" must be shown.
    * **Order Confirmation:** The final step shall display a detailed summary of the order (including service type, addresses, item category, and package specs), the calculated final price (itemized by service fee, taxes/fees, and insurance cost), and a clear, primary button to confirm and submit the order, initiating the secure payment gateway process. Prior to payment, the system shall require the user to input the Recipient's Contact Name and Recipient's Contact Phone Number for the drop-off location. These inputs must be validated for presence and phone format before enabling the payment button.

### 3.3 Real-Time Order Tracking
**Description:** The application must provide a dedicated mechanism for users to monitor parcel progress in real time.

* **3.3.1 Tracking Input:** The system shall provide a dedicated input interface, accessible via a "Track Order" link, that accepts a unique tracking identifier (e.g., Order ID).
    * **ID Validation:** The system shall validate the format and existence of the entered tracking ID on submission, providing a clear error state for invalid identifiers. Tracking ID format must adhere to a predefined alphanumeric pattern (e.g., BRZ-00000000). If invalid, the error message "Invalid Tracking ID format or ID not found" must be displayed below the input field.
* **3.3.2 Status Display:** Upon submission of a valid identifier, the system shall display the parcel's status, historical activity log, and estimated time of arrival (ETA).
    * **Map Visualization (Not required: Future planning):** The tracking display shall include a dynamic map component (e.g., leveraging a public mapping library) visualizing the real-time location of the assigned courier relative to the pickup and drop-off points. The map shall use distinct, identifiable markers for 'Pickup Location,' 'Drop-off Location,' and 'Courier Position'. Markers shall use distinct iconography: Pickup (Green pin), Drop-off (Red pin), and Courier (Dynamic icon representing vehicle type or a pulsing blue circle). Clicking the Courier marker shall reveal a tooltip with the courier's name and vehicle type.
    * **Auto-Refresh (Not required: Future planning):** The displayed location and status shall automatically refresh the data every 15 seconds without requiring a manual page reload or user intervention. A visible timestamp must be present to indicate the last successful data update time. If the automatic refresh fails (e.g., due to a network error), the timestamp shall turn red, and a "Retry Now" button shall appear.

### 3.4 Location and Region Management
**Description:** Users must be able to define and switch the regional focus of the application's content and service availability.

* **3.4.1 Active City Selector:** The system shall include a persistent, interactive city selector component that allows the user to switch the regional focus to any supported operating city (e.g., Pune, Mumbai, Delhi/NCR).
    * **State Persistence:** The user's city selection shall be stored persistently, preferably using Local Storage with a specific key (e.g., `xxx_user_city`), to ensure the choice persists across sessions. The key shall be `xxx_user_city_preference` and the value stored shall be the two-letter ISO country code followed by the city slug (e.g., IN-Pune). Changing the city shall trigger a full-page refresh.
    * **Visual Indication:** The system shall visually highlight the currently selected city (e.g., '📍 Pune') on the selector component and throughout the main page content to confirm the selection. All dynamic content, including pricing and FAQ answers, must reflect the selected city.
* **3.4.2 City Service Listing:** The application shall maintain an up-to-date list or map component that displays all operational cities where the delivery service is active.

### 3.5 Information and Support Access
**Description:** The application must provide clear and functional links to all necessary supporting documentation.

* **3.5.1 Documentation Access:** The system shall ensure functional hyperlinks are provided for all core informational pages including FAQs, History, Contacts, and the WebApp Blog.
* **3.5.2 Legal Access:** The system shall provide functional hyperlinks to all necessary policy and legal documentation (Privacy Policy, Terms and conditions, Refund and Cancellation Policy, and Disclaimers & Dispute Resolution).
    * **Link Behavior:** All external and informational links (e.g., WebApp Blog, Terms and Conditions) shall open in a new browser tab/window to maintain the current user session on the main application.

### 3.6 Partner/Courier Onboarding Interface
**Description:** The application must provide a channel for prospective independent contractors to apply to the network.

* **3.6.1 Courier Application Link:** The system shall feature a prominent link labeled "Become a courier" that redirects the user to a dedicated application submission portal.
    * **Mandatory Fields:** The application portal shall include mandatory input fields for Full Legal Name, Date of Birth (Age verification required: minimum 18 years old), Contact Information (Phone, Email, Current City), Vehicle Details (Type selection: Bike/Scooter, Car, Van), Vehicle Registration Number, and a field for Proof of Identity Upload (file input type supporting PDF/JPG/PNG, max file size 5MB). The "Proof of Identity Upload" field shall only accept files that are less than 5MB and must display a progress bar during upload. The submission button must enter a disabled "Uploading..." state during file processing.
    * **Consent:** The application process shall require explicit user consent regarding background checks and terms of service via a mandatory checkbox before enabling form submission.

### 3.7 Business Sales Inquiry Interface
**Description:** The application must provide a dedicated contact channel for potential business clients.

* **3.7.1 Sales Contact Link:** The system shall provide a dedicated link labeled "Contact sales" that redirects business users to a lead generation form.
    * **Lead Form:** The form shall require Business Name, Contact Person Full Name, Business Email (must validate format), Phone Number (must validate 10-digit Indian format), and a free-text field for describing their specific delivery needs (with a minimum character count of 50 and maximum of 500). The form submission button must be disabled until all mandatory fields are correctly filled. Upon successful submission, a temporary success message "Thank you, we will contact you shortly" must be displayed, and the form fields cleared.

## 4.0 Non-Functional Requirements (NFR)

### 4.1 Performance and Usability
* **4.1.2 Initial Load Time:** The main landing page content and interactive elements shall render fully within 3.0 seconds when accessed over a standard 4G network connection.
* **4.1.3 Responsiveness:** All user interfaces shall maintain full functionality and render correctly across viewport widths ranging from 320px (mobile) to 1920px (desktop).
* **4.1.4 Assignment Speed:** The system shall confirm courier assignment within a target maximum time of 120 seconds (2 minutes) from the user's final booking confirmation.
* **4.1.5 Accessibility:** The application shall adhere to WCAG 2.1 Level AA standards, particularly regarding screen reader compatibility and keyboard navigation.

### 4.2 Security and Service Assurance
* **4.2.1 Data Encryption:** All data transmissions between the client browser and the server shall be secured using TLS 1.2 or higher encryption protocols.
* **4.2.2 Data Integrity (Not required: Future planning):** The system shall ensure data integrity for live parcel tracking with a target accuracy of 99.8% (as per marketing claims), minimizing reporting errors or delays.
* **4.2.3 Financial Guarantee Visibility (Optional: Future planning):** The system shall clearly document and display the maximum insurance coverage amount (e.g., "Insure packages for up to ₹ 50,000") within the booking process.

### 4.3 Compliance and Extensibility
* **4.3.1 Cookie Compliance:** The application shall display a non-intrusive, interactive cookie consent banner upon the user's initial visit, allowing the user to manage their preferences.
* **4.3.2 API Extensibility (Not required: Future planning):** The application shall maintain a publicly accessible link to documentation detailing the available API Integration endpoints for third-party system connections.

## 5.0 Conclusion
These revised requirements document provides an in-depth, technical, and actionable definition of the WebApp Online Delivery Web Application's frontend scope. By expanding each functional requirement to include specific input validation rules, mandatory data fields, and detailed interaction logic (e.g., the multi-step booking workflow, inline modal behavior), this document is now suitable for direct use by the development and quality assurance teams without requiring external references.