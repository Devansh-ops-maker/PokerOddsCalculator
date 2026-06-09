async function calculateProbability() {

    const playerCards =
        document.getElementById("playerCards").value;

    const communityCards =
        document.getElementById("communityCards").value;

    const totalPlayers =
        document.getElementById("totalPlayers").value;

    const response = await fetch(

        `/probability?player_cards=${playerCards}&comm_cards=${communityCards}&total_players=${totalPlayers}`

    );

    const data = await response.json();

    document.getElementById("result").innerHTML =

        `Winning Probability: ${(data.probability * 100).toFixed(2)}%`;
}