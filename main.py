import hashlib

def hash_vote(candidate):
    """Create a hash of the vote to prevent tampering."""
    return hashlib.sha256(candidate.encode()).hexdigest()

def register_voter(voters, voter_id):
    """Register a voter if not already registered."""
    if voter_id not in voters:
        voters[voter_id] = False  # False indicates the voter has not voted
        print(f"Voter {voter_id} registered.")
    else:
        print(f"Voter {voter_id} is already registered.")

def add_candidate(candidates, candidate):
    """Add a candidate to the voting list."""
    if candidate not in candidates:
        candidates.append(candidate)
        print(f"Candidate {candidate} added.")
    else:
        print(f"Candidate {candidate} is already in the list.")

def cast_vote(voters, votes, voter_id, candidate, candidates):
    """Cast a vote for a candidate."""
    if voter_id not in voters:
        print("Voter not registered.")
        return
    if voters[voter_id]:
        print("Voter has already voted.")
        return
    if candidate not in candidates:
        print("Candidate not found.")
        return

    votes.append(candidate)  # Store the candidate directly
    voters[voter_id] = True  # Mark the voter as having voted
    print(f"Vote cast for {candidate} by voter {voter_id}.")

def tally_votes(votes):
    """Tally the votes and return the results."""
    results = {}
    for vote in votes:
        if vote in results:
            results[vote] += 1
        else:
            results[vote] = 1
    return results

def main():
    voters = {}
    candidates = []
    votes = []

    while True:
        print("\nMenu:")
        print("1: Register Voter")
        print("2: Add Candidate")
        print("3: Cast Vote")
        print("4: Show Results")
        print("5: Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            voter_id = input("Enter voter ID: ")
            register_voter(voters, voter_id)
        elif choice == '2':
            candidate = input("Enter candidate name: ")
            add_candidate(candidates, candidate)
        elif choice == '3':
            voter_id = input("Enter voter ID: ")
            candidate = input("Enter candidate name: ")
            cast_vote(voters, votes, voter_id, candidate, candidates)
        elif choice == '4':
            results = tally_votes(votes)
            print("Vote results:", results)
        elif choice == '5':
            print("Exiting the voting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

