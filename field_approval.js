const nodemailer = require('nodemailer');

// Function to send an approval request to the field manager
function sendApprovalRequest(payload) {
  // Create a transporter to send the email
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'your_email@gmail.com',
      pass: 'your_email_password'
    }
  });

  // Create the email message
  const message = {
    from: 'your_email@gmail.com',
    to: 'field_manager_email@example.com',
    subject: 'Approval request for fielding pictures/documents',
    html: `<p>Dear Field Manager,</p>
           <p>You have a new approval request for fielding pictures/documents:</p>
           <ul>
             <li>Fielding ID: ${payload.fieldingId}</li>
             <li>Fielding Type: ${payload.fieldingType}</li>
             <li>Fielding Date: ${payload.fieldingDate}</li>
           </ul>
           <p>Please click the following link to approve or reject the request:</p>
           <a href="http://yourapp.com/approve?id=${payload.fieldingId}&type=${payload.fieldingType}&date=${payload.fieldingDate}">Approve/Reject</a>`
  };

  // Send the email
  transporter.sendMail(message, (error, info) => {
    if (error) {
      console.log(error);
    } else {
      console.log('Email sent: ' + info.response);
    }
  });
}
