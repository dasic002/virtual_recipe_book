const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("comment_form");
const commentSubmitBtn = document.getElementById("commentSubmitButton");
const commentCancelBtn = document.getElementById("commentCancelButton");

const ratingText = document.getElementById("id_review");
const ratingForm = document.getElementById("rating_form");
const ratingSubmitBtn = document.getElementById("ratingSubmitButton");
const ratingCancelBtn = document.getElementById("ratingCancelButton");
const userRating = document.getElementById("userRating");
const ratingEditor = document.getElementById("ratingEditor");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteType = document.getElementsByClassName("object-type");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 *
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.currentTarget.getAttribute("data-comment-id");
    let ratingId = e.currentTarget.getAttribute("data-rating-id");

    if (ratingId) {
      let ratingContent = document.getElementById("userRatingBody").innerText;
      let score = document
        .getElementById("userRatingBody")
        .getAttribute("data-score");
      userRating.hidden = true;
      ratingEditor.hidden = false;
      ratingText.value = ratingContent;
      document.getElementById(`id_score_${score - 1}`).checked = true;
      ratingSubmitBtn.innerText = "Update";
      ratingCancelBtn.hidden = false;
      ratingForm.setAttribute("action", `edit-rating/${ratingId}`);
      ratingForm.querySelector("textarea").focus();
    } else {
      let commentContent = document.getElementById(
        `comment${commentId}`
      ).innerText;
      commentText.value = commentContent;
      commentSubmitBtn.innerText = "Update";
      commentCancelBtn.hidden = false;
      commentForm.setAttribute("action", `edit-comment/${commentId}`);
      commentForm.querySelector("textarea").focus();
    }
  });
}

/**
 * Initializes cancel functionality for the provided cancel buttons.
 */
commentCancelBtn.addEventListener("click", (e) => {
  commentForm.reset();
  commentSubmitBtn.innerText = "Submit";
  commentCancelBtn.hidden = true;
  commentForm.removeAttribute("action");
});

ratingCancelBtn.addEventListener("click", (e) => {
  ratingForm.reset();
  ratingSubmitBtn.innerText = "Submit";
  ratingCancelBtn.hidden = true;
  ratingForm.removeAttribute("action");
  if (userRating) {
    ratingEditor.hidden = true;
    userRating.hidden = false;
  }
});

/**
 * Initializes deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.currentTarget.getAttribute("data-comment-id");
    let ratingId = e.currentTarget.getAttribute("data-rating-id");
    deleteConfirm.href = ratingId
      ? `delete-rating/${ratingId}`
      : `delete-comment/${commentId}`;
    
    for (let type of deleteType) {
      if (ratingId) {
        type.innerText = "rating";
      } else {
        type.innerText = "comment";
      }
    }
    deleteModal.show();
  });
}
