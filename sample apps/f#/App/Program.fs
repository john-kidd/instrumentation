open System.Diagnostics
open System 

// command and query decorators
// the decorators act like a russian doll where each layer adds more functionality around the command or query 
let queryTimer logger (func: unit -> 'T) description: 'T =
    let sw = new System.Diagnostics.Stopwatch()
    sw.Start()
    let result = func()
    sw.Stop()
    logger ("DURATION " + description() + " took " + sw.Elapsed.Milliseconds.ToString() + " milliseconds")
    result

let commandTimer logger action description =
    let sw = new System.Diagnostics.Stopwatch()
    sw.Start()
    action()
    sw.Stop()
    logger ("DURATION " + description() + " took " + sw.Elapsed.Milliseconds.ToString() + " milliseconds")

let queryHandler logger (func: unit -> 'T) description: 'T =
    logger ("BEGIN " + description())
    let query = queryTimer logger
    let result = query func description
    logger("END " + description())
    result

let commandHandler logger action description =
    logger ("BEGIN " + description())
    let command = commandTimer logger
    command action description
    logger("END " + description())

// we use option here because we need return None if an error is handled and we compensate
let queryCompensator logger (func: unit -> 'T) description: 'T option =
    try
        let query = queryHandler logger
        let result = query func description
        Some(result)
    with
    | ex ->
        logger("FAILED " + description())
        logger ex.Message
        None

let commandCompensator logger action description =
    try
        let command = commandHandler logger
        command action description
    with
    | ex ->
        logger("FAILED " + description())
        logger ex.Message

let logger m = printfn "%s" m
 
type Contact = {
    name: string;
    email: string
}
 
// test our command and query decorators
let queryContactsTest =
    let query = queryCompensator logger
    let result = query (fun () -> { name = "JFK"; email = "jfk@test.com" }) (fun () -> "query 1")
 
    match result with
    | Some x -> printfn "Data: %s %s" x.name x.email
    | None -> printfn "No value"
 
let queryErroredTest =
    let query = queryCompensator logger
    let result = query (fun () -> raise(new System.InvalidOperationException("query 2 error"))) (fun () -> "query 2")
 
    match result with
    | Some x -> printfn "Data: %A" x
    | None -> printfn "Invalid Operation Error"
 
let queryIntTest =
    let query = queryCompensator logger
    let result = query (fun () -> 1234) (fun () -> "query 3")
 
    match result with
    | Some x -> printfn "Data: %A" x
    | None -> printfn "No value"
 
let commandTest =
    let execute = commandCompensator logger
    execute (fun () -> printfn "Action: 1") (fun () -> "action 1")
 
let commandErroredTest =
    let execute = commandCompensator logger
    execute (fun () -> raise(new System.InvalidOperationException("Action: 2 errored"))) (fun () -> "action 2")
 
 
[<EntryPoint>]
let main argv =
    queryContactsTest
    queryErroredTest
    queryIntTest
    commandTest
    commandErroredTest
 
    Console.ReadKey() |> ignore
 
    0    