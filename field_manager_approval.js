// create a route for handling the approval link that the field manager clicks in the email. 
// route will update the status of the fielding pictures or documents in the database based on the field manager's approval or rejection.

// Define a route for handling approval links
app.get('/approve', (req, res) => {
  const fieldingId = req.query.id;
  const fieldingType = req.query.type;
  const fieldingDate = req.query.date;
  const approved = req.query.approved === 'true';

  // Update the status of the fielding pictures/documents in the database
  updateFieldingStatus(fieldingId, fieldingType, fieldingDate, approved);

